# InventoryHasStandardAloneHosts

A InventoryHasStandardAloneHosts fault is thrown if an assignment operation tries to downgrade a license that does have allow hosts licensed with StandardAlone license in the inventory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** |  | 

## Example

```python
from vmware_vi.models.inventory_has_standard_alone_hosts import InventoryHasStandardAloneHosts

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryHasStandardAloneHosts from a JSON string
inventory_has_standard_alone_hosts_instance = InventoryHasStandardAloneHosts.from_json(json)
# print the JSON string representation of the object
print InventoryHasStandardAloneHosts.to_json()

# convert the object into a dict
inventory_has_standard_alone_hosts_dict = inventory_has_standard_alone_hosts_instance.to_dict()
# create an instance of InventoryHasStandardAloneHosts from a dict
inventory_has_standard_alone_hosts_form_dict = inventory_has_standard_alone_hosts.from_dict(inventory_has_standard_alone_hosts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


