# ConvertNamespacePathToUuidPathRequestType

The parameters of *DatastoreNamespaceManager.ConvertNamespacePathToUuidPath*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**namespace_url** | **str** | Namesapce URL of the form &gt; \\[ds://\\]/vmfs/volumes/\\[_datastore-uuid_\\]/\\[_directory-name_\\]/... &gt;  | 

## Example

```python
from vmware_vi.models.convert_namespace_path_to_uuid_path_request_type import ConvertNamespacePathToUuidPathRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertNamespacePathToUuidPathRequestType from a JSON string
convert_namespace_path_to_uuid_path_request_type_instance = ConvertNamespacePathToUuidPathRequestType.from_json(json)
# print the JSON string representation of the object
print ConvertNamespacePathToUuidPathRequestType.to_json()

# convert the object into a dict
convert_namespace_path_to_uuid_path_request_type_dict = convert_namespace_path_to_uuid_path_request_type_instance.to_dict()
# create an instance of ConvertNamespacePathToUuidPathRequestType from a dict
convert_namespace_path_to_uuid_path_request_type_form_dict = convert_namespace_path_to_uuid_path_request_type.from_dict(convert_namespace_path_to_uuid_path_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


