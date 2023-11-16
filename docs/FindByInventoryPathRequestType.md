# FindByInventoryPathRequestType

The parameters of *SearchIndex.FindByInventoryPath*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_path** | **str** | The path to the entity.  | 

## Example

```python
from vmware_vi.models.find_by_inventory_path_request_type import FindByInventoryPathRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindByInventoryPathRequestType from a JSON string
find_by_inventory_path_request_type_instance = FindByInventoryPathRequestType.from_json(json)
# print the JSON string representation of the object
print FindByInventoryPathRequestType.to_json()

# convert the object into a dict
find_by_inventory_path_request_type_dict = find_by_inventory_path_request_type_instance.to_dict()
# create an instance of FindByInventoryPathRequestType from a dict
find_by_inventory_path_request_type_form_dict = find_by_inventory_path_request_type.from_dict(find_by_inventory_path_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


