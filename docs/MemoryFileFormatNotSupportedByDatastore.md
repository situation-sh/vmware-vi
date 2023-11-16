# MemoryFileFormatNotSupportedByDatastore

Virtual memory file format is not supported on the datastore.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_name** | **str** | The name of the Datastore.  ***Since:*** vSphere API 6.0  | 
**type** | **str** | Datastore file system volume type.  See *DatastoreSummary.type*  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.memory_file_format_not_supported_by_datastore import MemoryFileFormatNotSupportedByDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryFileFormatNotSupportedByDatastore from a JSON string
memory_file_format_not_supported_by_datastore_instance = MemoryFileFormatNotSupportedByDatastore.from_json(json)
# print the JSON string representation of the object
print MemoryFileFormatNotSupportedByDatastore.to_json()

# convert the object into a dict
memory_file_format_not_supported_by_datastore_dict = memory_file_format_not_supported_by_datastore_instance.to_dict()
# create an instance of MemoryFileFormatNotSupportedByDatastore from a dict
memory_file_format_not_supported_by_datastore_form_dict = memory_file_format_not_supported_by_datastore.from_dict(memory_file_format_not_supported_by_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


