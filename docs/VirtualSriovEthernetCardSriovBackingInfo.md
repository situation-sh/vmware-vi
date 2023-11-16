# VirtualSriovEthernetCardSriovBackingInfo

The *VirtualSriovEthernetCardSriovBackingInfo* data object contains information about the SR-IOV physical function and virtual function backing for a passthrough NIC.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**physical_function_backing** | [**VirtualPCIPassthroughDeviceBackingInfo**](VirtualPCIPassthroughDeviceBackingInfo.md) |  | [optional] 
**virtual_function_backing** | [**VirtualPCIPassthroughDeviceBackingInfo**](VirtualPCIPassthroughDeviceBackingInfo.md) |  | [optional] 
**virtual_function_index** | **int** |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_sriov_ethernet_card_sriov_backing_info import VirtualSriovEthernetCardSriovBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSriovEthernetCardSriovBackingInfo from a JSON string
virtual_sriov_ethernet_card_sriov_backing_info_instance = VirtualSriovEthernetCardSriovBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualSriovEthernetCardSriovBackingInfo.to_json()

# convert the object into a dict
virtual_sriov_ethernet_card_sriov_backing_info_dict = virtual_sriov_ethernet_card_sriov_backing_info_instance.to_dict()
# create an instance of VirtualSriovEthernetCardSriovBackingInfo from a dict
virtual_sriov_ethernet_card_sriov_backing_info_form_dict = virtual_sriov_ethernet_card_sriov_backing_info.from_dict(virtual_sriov_ethernet_card_sriov_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


