# DVSMacManagementPolicy

This data object type describes MAC management policy of a port.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_promiscuous** | **bool** | The flag to indicate whether or not all traffic is seen on the port.  ***Since:*** vSphere API 6.7  | [optional] 
**mac_changes** | **bool** | The flag to indicate whether or not the Media Access Control (MAC) address can be changed.  ***Since:*** vSphere API 6.7  | [optional] 
**forged_transmits** | **bool** | The flag to indicate whether or not the virtual network adapter should be allowed to send network traffic with a different MAC address than that of the virtual network adapter.  ***Since:*** vSphere API 6.7  | [optional] 
**mac_learning_policy** | [**DVSMacLearningPolicy**](DVSMacLearningPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.dvs_mac_management_policy import DVSMacManagementPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSMacManagementPolicy from a JSON string
dvs_mac_management_policy_instance = DVSMacManagementPolicy.from_json(json)
# print the JSON string representation of the object
print DVSMacManagementPolicy.to_json()

# convert the object into a dict
dvs_mac_management_policy_dict = dvs_mac_management_policy_instance.to_dict()
# create an instance of DVSMacManagementPolicy from a dict
dvs_mac_management_policy_form_dict = dvs_mac_management_policy.from_dict(dvs_mac_management_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


