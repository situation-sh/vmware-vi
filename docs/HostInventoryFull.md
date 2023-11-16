# HostInventoryFull

A HostInventoryFull is thrown if the inventory has reach the max capacity of hosts.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** |  | 

## Example

```python
from vmware_vi.models.host_inventory_full import HostInventoryFull

# TODO update the JSON string below
json = "{}"
# create an instance of HostInventoryFull from a JSON string
host_inventory_full_instance = HostInventoryFull.from_json(json)
# print the JSON string representation of the object
print HostInventoryFull.to_json()

# convert the object into a dict
host_inventory_full_dict = host_inventory_full_instance.to_dict()
# create an instance of HostInventoryFull from a dict
host_inventory_full_form_dict = host_inventory_full.from_dict(host_inventory_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


