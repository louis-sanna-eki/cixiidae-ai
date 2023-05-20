import pandas as pd
import json

# Field configuration
fields = [
        {
            "fid": "gbifID",
            "semanticType": "nominal"
        },
        {
            "fid": "datasetKey",
            "semanticType": "nominal"
        },
        {
            "fid": "occurrenceID",
            "semanticType": "nominal"
        },
        {
            "fid": "kingdom",
            "semanticType": "nominal"
        },
        {
            "fid": "phylum",
            "semanticType": "nominal"
        },
        {
            "fid": "class",
            "semanticType": "nominal"
        },
        {
            "fid": "order",
            "semanticType": "nominal"
        },
        {
            "fid": "family",
            "semanticType": "nominal"
        },
        {
            "fid": "genus",
            "semanticType": "nominal"
        },
        {
            "fid": "species",
            "semanticType": "nominal"
        },
        {
            "fid": "infraspecificEpithet",
            "semanticType": "nominal"
        },
        {
            "fid": "taxonRank",
            "semanticType": "nominal"
        },
        {
            "fid": "scientificName",
            "semanticType": "nominal"
        },
        {
            "fid": "verbatimScientificName",
            "semanticType": "nominal"
        },
        {
            "fid": "verbatimScientificNameAuthorship",
            "semanticType": "nominal"
        },
        {
            "fid": "countryCode",
            "semanticType": "nominal"
        },
        {
            "fid": "locality",
            "semanticType": "nominal"
        },
        {
            "fid": "stateProvince",
            "semanticType": "nominal"
        },
        {
            "fid": "occurrenceStatus",
            "semanticType": "nominal"
        },
        {
            "fid": "individualCount",
            "semanticType": "quantitative"
        },
        {
            "fid": "publishingOrgKey",
            "semanticType": "nominal"
        },
        {
            "fid": "decimalLatitude",
            "semanticType": "quantitative"
        },
        {
            "fid": "decimalLongitude",
            "semanticType": "quantitative"
        },
        {
            "fid": "coordinateUncertaintyInMeters",
            "semanticType": "quantitative"
        },
        {
            "fid": "coordinatePrecision",
            "semanticType": "quantitative"
        },
        {
            "fid": "elevation",
            "semanticType": "quantitative"
        },
        {
            "fid": "elevationAccuracy",
            "semanticType": "quantitative"
        },
        {
            "fid": "depth",
            "semanticType": "quantitative"
        },
        {
            "fid": "depthAccuracy",
            "semanticType": "quantitative"
        },
        {
            "fid": "eventDate",
            "semanticType": "temporal"
        },
        {
            "fid": "day",
            "semanticType": "temporal"
        },
        {
            "fid": "month",
            "semanticType": "temporal"
        },
        {
            "fid": "year",
            "semanticType": "temporal"
        },
        {
            "fid": "taxonKey",
            "semanticType": "nominal"
        },
        {
            "fid": "speciesKey",
            "semanticType": "nominal"
        },
        {
            "fid": "basisOfRecord",
            "semanticType": "nominal"
        },
        {
            "fid": "institutionCode",
            "semanticType": "nominal"
        },
        {
            "fid": "collectionCode",
            "semanticType": "nominal"
        },
        {
            "fid": "catalogNumber",
            "semanticType": "nominal"
        },
        {
            "fid": "recordNumber",
            "semanticType": "nominal"
        },
        {
            "fid": "identifiedBy",
            "semanticType": "nominal"
        },
        {
            "fid": "dateIdentified",
            "semanticType": "temporal"
        },
        {
            "fid": "license",
            "semanticType": "nominal"
        },
        {
            "fid": "rightsHolder",
            "semanticType": "nominal"
        },
        {
            "fid": "recordedBy",
            "semanticType": "nominal"
        },
        {
            "fid": "typeStatus",
            "semanticType": "nominal"
        },
        {
            "fid": "establishmentMeans",
            "semanticType": "nominal"
        },
        {
            "fid": "lastInterpreted",
            "semanticType": "temporal"
        },
        {
            "fid": "mediaType",
            "semanticType": "nominal"
        },
        {
            "fid": "issue",
            "semanticType": "nominal"
        }
    ]

# Read the CSV data
df = pd.read_csv(
    'input.csv',
    error_bad_lines=False,
    sep='\t',
    low_memory=False
)

# Store initial column names
initial_columns = df.columns

# Drop columns with any NaN values
df = df.dropna(axis=1)

# Find the names of the columns that got dropped
dropped_columns = [col for col in initial_columns if col not in df.columns]
print("Dropped columns: ", dropped_columns)

# Convert the DataFrame to a list of dictionaries
data_source = df.to_dict('records')

# Construct the final JSON structure
final_json = {
    "fields": fields,
    "dataSource": data_source
}

# Write the final JSON structure to a file
with open('output.json', 'w') as f:
    json.dump(final_json, f)
