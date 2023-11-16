# HostPcieTargetTransport

Peripheral Component Interconnect Express (PCIe) transport information about a target.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_pcie_target_transport import HostPcieTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of HostPcieTargetTransport from a JSON string
host_pcie_target_transport_instance = HostPcieTargetTransport.from_json(json)
# print the JSON string representation of the object
print HostPcieTargetTransport.to_json()

# convert the object into a dict
host_pcie_target_transport_dict = host_pcie_target_transport_instance.to_dict()
# create an instance of HostPcieTargetTransport from a dict
host_pcie_target_transport_form_dict = host_pcie_target_transport.from_dict(host_pcie_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


