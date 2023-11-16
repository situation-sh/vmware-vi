# DVSPolicy

The switch usage policy types  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_pre_install_allowed** | **bool** | Whether downloading a new proxy VirtualSwitch module to the host is allowed to be automatically executed by the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**auto_upgrade_allowed** | **bool** | Whether upgrading of the switch is allowed to be automatically executed by the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**partial_upgrade_allowed** | **bool** | Whether to allow upgrading a switch when some of the hosts failed to install the needed module.  The vCenter Server will reattempt the pre-install operation of the host module on those failed hosts, whenever they reconnect to vCenter.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_policy import DVSPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSPolicy from a JSON string
dvs_policy_instance = DVSPolicy.from_json(json)
# print the JSON string representation of the object
print DVSPolicy.to_json()

# convert the object into a dict
dvs_policy_dict = dvs_policy_instance.to_dict()
# create an instance of DVSPolicy from a dict
dvs_policy_form_dict = dvs_policy.from_dict(dvs_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


