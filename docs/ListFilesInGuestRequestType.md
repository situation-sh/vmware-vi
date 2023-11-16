# ListFilesInGuestRequestType

The parameters of *GuestFileManager.ListFilesInGuest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**auth** | [**GuestAuthentication**](GuestAuthentication.md) |  | 
**file_path** | **str** | The complete path to the directory or file to query.  | 
**index** | **int** | Which result to start the list with. The default is 0.  | [optional] 
**max_results** | **int** | The maximum number of results to return. The default is 50.  | [optional] 
**match_pattern** | **str** | A filter for the return values. Match patterns are specified using perl-compatible regular expressions. If matchPattern is unset, then the pattern &#39;.\\*&#39; is used.  | [optional] 

## Example

```python
from vmware_vi.models.list_files_in_guest_request_type import ListFilesInGuestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListFilesInGuestRequestType from a JSON string
list_files_in_guest_request_type_instance = ListFilesInGuestRequestType.from_json(json)
# print the JSON string representation of the object
print ListFilesInGuestRequestType.to_json()

# convert the object into a dict
list_files_in_guest_request_type_dict = list_files_in_guest_request_type_instance.to_dict()
# create an instance of ListFilesInGuestRequestType from a dict
list_files_in_guest_request_type_form_dict = list_files_in_guest_request_type.from_dict(list_files_in_guest_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


