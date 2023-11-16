# CreateFolderRequestType

The parameters of *Folder.CreateFolder*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to be given the new folder. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\\\\) and percent (%) will be escaped using the URL syntax. For example, %2F. Any percent (%) character used in this parameter must be escaped, unless it is used to start an escape sequence. Clients may also escape any other characters in this parameter.  | 

## Example

```python
from vmware_vi.models.create_folder_request_type import CreateFolderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolderRequestType from a JSON string
create_folder_request_type_instance = CreateFolderRequestType.from_json(json)
# print the JSON string representation of the object
print CreateFolderRequestType.to_json()

# convert the object into a dict
create_folder_request_type_dict = create_folder_request_type_instance.to_dict()
# create an instance of CreateFolderRequestType from a dict
create_folder_request_type_form_dict = create_folder_request_type.from_dict(create_folder_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


