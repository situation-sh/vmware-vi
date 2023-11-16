# HostFibreChannelOverEthernetHba

This data object type describes the FCoE host bus adapter interface.  Terminology is borrowed from T11's working draft of the Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**underlying_nic** | **str** | The name associated with this FCoE HBA&#39;s underlying FcoeNic.  ***Since:*** vSphere API 5.0  | 
**link_info** | [**HostFibreChannelOverEthernetHbaLinkInfo**](HostFibreChannelOverEthernetHbaLinkInfo.md) |  | 
**is_software_fcoe** | **bool** | True if this host bus adapter is a software based FCoE initiator.  ***Since:*** vSphere API 5.0  | 
**marked_for_removal** | **bool** | Deprecated as of vSphere API 8.0. Software FCoE not supported.  True if this host bus adapter has been marked for removal.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.host_fibre_channel_over_ethernet_hba import HostFibreChannelOverEthernetHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostFibreChannelOverEthernetHba from a JSON string
host_fibre_channel_over_ethernet_hba_instance = HostFibreChannelOverEthernetHba.from_json(json)
# print the JSON string representation of the object
print HostFibreChannelOverEthernetHba.to_json()

# convert the object into a dict
host_fibre_channel_over_ethernet_hba_dict = host_fibre_channel_over_ethernet_hba_instance.to_dict()
# create an instance of HostFibreChannelOverEthernetHba from a dict
host_fibre_channel_over_ethernet_hba_form_dict = host_fibre_channel_over_ethernet_hba.from_dict(host_fibre_channel_over_ethernet_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


