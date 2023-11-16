# ResetListViewFromViewRequestType

The parameters of *ListView.ResetListViewFromView*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.reset_list_view_from_view_request_type import ResetListViewFromViewRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResetListViewFromViewRequestType from a JSON string
reset_list_view_from_view_request_type_instance = ResetListViewFromViewRequestType.from_json(json)
# print the JSON string representation of the object
print ResetListViewFromViewRequestType.to_json()

# convert the object into a dict
reset_list_view_from_view_request_type_dict = reset_list_view_from_view_request_type_instance.to_dict()
# create an instance of ResetListViewFromViewRequestType from a dict
reset_list_view_from_view_request_type_form_dict = reset_list_view_from_view_request_type.from_dict(reset_list_view_from_view_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


