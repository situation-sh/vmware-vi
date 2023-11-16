# VspanPortPromiscChangeFault

Thrown when changing a non-promiscuous port used as tranmistted source or dest ports in Distributed Port Mirroring session to promiscuous mode.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **str** | The key of the port.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_port_promisc_change_fault import VspanPortPromiscChangeFault

# TODO update the JSON string below
json = "{}"
# create an instance of VspanPortPromiscChangeFault from a JSON string
vspan_port_promisc_change_fault_instance = VspanPortPromiscChangeFault.from_json(json)
# print the JSON string representation of the object
print VspanPortPromiscChangeFault.to_json()

# convert the object into a dict
vspan_port_promisc_change_fault_dict = vspan_port_promisc_change_fault_instance.to_dict()
# create an instance of VspanPortPromiscChangeFault from a dict
vspan_port_promisc_change_fault_form_dict = vspan_port_promisc_change_fault.from_dict(vspan_port_promisc_change_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


