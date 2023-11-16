# FcoeFaultPnicHasNoPortSet

Deprecated as of vSphere API 8.0. Software FCoE not supported.  This fault indicates the given Software Fcoe NIC has no uplink ports that is required for initiating a discovery.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.fcoe_fault_pnic_has_no_port_set import FcoeFaultPnicHasNoPortSet

# TODO update the JSON string below
json = "{}"
# create an instance of FcoeFaultPnicHasNoPortSet from a JSON string
fcoe_fault_pnic_has_no_port_set_instance = FcoeFaultPnicHasNoPortSet.from_json(json)
# print the JSON string representation of the object
print FcoeFaultPnicHasNoPortSet.to_json()

# convert the object into a dict
fcoe_fault_pnic_has_no_port_set_dict = fcoe_fault_pnic_has_no_port_set_instance.to_dict()
# create an instance of FcoeFaultPnicHasNoPortSet from a dict
fcoe_fault_pnic_has_no_port_set_form_dict = fcoe_fault_pnic_has_no_port_set.from_dict(fcoe_fault_pnic_has_no_port_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


