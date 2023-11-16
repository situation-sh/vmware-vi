# ArrayOfInventoryDescription

A boxed array of *InventoryDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InventoryDescription]**](InventoryDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_inventory_description import ArrayOfInventoryDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInventoryDescription from a JSON string
array_of_inventory_description_instance = ArrayOfInventoryDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfInventoryDescription.to_json()

# convert the object into a dict
array_of_inventory_description_dict = array_of_inventory_description_instance.to_dict()
# create an instance of ArrayOfInventoryDescription from a dict
array_of_inventory_description_form_dict = array_of_inventory_description.from_dict(array_of_inventory_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


