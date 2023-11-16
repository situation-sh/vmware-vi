# CreateListViewFromViewRequestType

The parameters of *ViewManager.CreateListViewFromView*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.create_list_view_from_view_request_type import CreateListViewFromViewRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateListViewFromViewRequestType from a JSON string
create_list_view_from_view_request_type_instance = CreateListViewFromViewRequestType.from_json(json)
# print the JSON string representation of the object
print CreateListViewFromViewRequestType.to_json()

# convert the object into a dict
create_list_view_from_view_request_type_dict = create_list_view_from_view_request_type_instance.to_dict()
# create an instance of CreateListViewFromViewRequestType from a dict
create_list_view_from_view_request_type_form_dict = create_list_view_from_view_request_type.from_dict(create_list_view_from_view_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


