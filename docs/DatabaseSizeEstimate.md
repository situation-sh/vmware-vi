# DatabaseSizeEstimate

DatabaseSizeEstimate contains information about the size required to by the database.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The estimated size required in MB  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.database_size_estimate import DatabaseSizeEstimate

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSizeEstimate from a JSON string
database_size_estimate_instance = DatabaseSizeEstimate.from_json(json)
# print the JSON string representation of the object
print DatabaseSizeEstimate.to_json()

# convert the object into a dict
database_size_estimate_dict = database_size_estimate_instance.to_dict()
# create an instance of DatabaseSizeEstimate from a dict
database_size_estimate_form_dict = database_size_estimate.from_dict(database_size_estimate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


