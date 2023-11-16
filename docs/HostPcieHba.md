# HostPcieHba

This data object describes the Peripheral Component Interconnect Express (PCIe) host bus adapter interface.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_pcie_hba import HostPcieHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostPcieHba from a JSON string
host_pcie_hba_instance = HostPcieHba.from_json(json)
# print the JSON string representation of the object
print HostPcieHba.to_json()

# convert the object into a dict
host_pcie_hba_dict = host_pcie_hba_instance.to_dict()
# create an instance of HostPcieHba from a dict
host_pcie_hba_form_dict = host_pcie_hba.from_dict(host_pcie_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


