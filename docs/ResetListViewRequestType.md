# ResetListViewRequestType

The parameters of *ListView.ResetListView*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The new list of objects.  ***Required privileges:*** System.View  | [optional] 

## Example

```python
from vmware_vi.models.reset_list_view_request_type import ResetListViewRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResetListViewRequestType from a JSON string
reset_list_view_request_type_instance = ResetListViewRequestType.from_json(json)
# print the JSON string representation of the object
print ResetListViewRequestType.to_json()

# convert the object into a dict
reset_list_view_request_type_dict = reset_list_view_request_type_instance.to_dict()
# create an instance of ResetListViewRequestType from a dict
reset_list_view_request_type_form_dict = reset_list_view_request_type.from_dict(reset_list_view_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


