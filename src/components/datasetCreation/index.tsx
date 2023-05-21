import { useCallback, useRef, useState } from "react";
import { produce } from "immer";
import { IDataset, IRow } from "../../interface";
import { FileReader } from "@kanaries/web-data-loader";
import { inferDatasetMeta } from "../../utils/inferType";
import Modal from "../modal";
import DataTable from "./dataTable";

interface DatasetCreationProps {
    onDatasetCreated: (dataset: IDataset) => void;
}

export default function DatasetCreation(props: DatasetCreationProps) {
    const { onDatasetCreated } = props;
    const fileRef = useRef<HTMLInputElement>(null);
    const [modalOpen, setModalOpen] = useState(false);
    const [tmpDataset, setTmpDataset] = useState<IDataset | null>(null);

    const fileUpload = useCallback(
        (e: React.ChangeEvent<HTMLInputElement>) => {
            const files = e.target.files;
            if (files !== null) {
                const file = files[0];
                FileReader.csvReader({
                    file,
                    config: { type: "reservoirSampling", size: Infinity },
                    encoding: 'utf-8'
                }).then((data) => {
                    const dataset = inferDatasetMeta(data as IRow[]);
                    // onDatasetCreated(dataset);
                    setModalOpen(true);
                    setTmpDataset(dataset);
                });
            }
        },
        []
    );

    return (
        <div>
            <button
                type="button"
                className="ml-4 rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600"
                onClick={() => {
                    fileRef.current?.click();
                }}
            >
                Upload CSV
            </button>
            <input
                type="file"
                ref={fileRef}
                className="hidden"
                onChange={fileUpload}
            />
            <Modal
                show={modalOpen}
                onClose={() => {
                    setModalOpen(false);
                }}
            >
                {tmpDataset && (
                    <DataTable
                        data={tmpDataset.dataSource}
                        metas={tmpDataset.fields}
                        onMetaChange={(fid, fIndex, meta) => {
                            const nextDataset = produce(tmpDataset, (draft) => {
                                draft.fields[fIndex] = {
                                    ...draft.fields[fIndex],
                                    ...meta,
                                };
                            });
                            setTmpDataset(nextDataset);
                        }}
                    />
                )}
                <div>
                    <button
                        type="button"
                        className="ml-4 rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-green-600"
                        onClick={() => {
                            if (tmpDataset) {
                                onDatasetCreated(tmpDataset as IDataset);
                            }
                            setModalOpen(false);
                        }}
                    >
                        Confirm
                    </button>
                </div>
            </Modal>
        </div>
    );
}
