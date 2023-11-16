# VMOnVirtualIntranet

The virtual machine is using a \"virtual intranet\", a virtual network that exists only within a single host.  If returned as part of a migration check, this is an error if the virtual machine is currently connected to the network and a warning otherwise. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmon_virtual_intranet import VMOnVirtualIntranet

# TODO update the JSON string below
json = "{}"
# create an instance of VMOnVirtualIntranet from a JSON string
vmon_virtual_intranet_instance = VMOnVirtualIntranet.from_json(json)
# print the JSON string representation of the object
print VMOnVirtualIntranet.to_json()

# convert the object into a dict
vmon_virtual_intranet_dict = vmon_virtual_intranet_instance.to_dict()
# create an instance of VMOnVirtualIntranet from a dict
vmon_virtual_intranet_form_dict = vmon_virtual_intranet.from_dict(vmon_virtual_intranet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


