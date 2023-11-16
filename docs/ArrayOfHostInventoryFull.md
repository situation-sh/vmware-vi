# ArrayOfHostInventoryFull

A boxed array of *HostInventoryFull*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostInventoryFull]**](HostInventoryFull.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_inventory_full import ArrayOfHostInventoryFull

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostInventoryFull from a JSON string
array_of_host_inventory_full_instance = ArrayOfHostInventoryFull.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostInventoryFull.to_json()

# convert the object into a dict
array_of_host_inventory_full_dict = array_of_host_inventory_full_instance.to_dict()
# create an instance of ArrayOfHostInventoryFull from a dict
array_of_host_inventory_full_form_dict = array_of_host_inventory_full.from_dict(array_of_host_inventory_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


