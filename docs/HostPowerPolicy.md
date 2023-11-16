# HostPowerPolicy

Power Management Policy data object.  Used to retrieve and specify current host power management policy.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | Power Policy Key.  Internally generated key which uniquely identifies power management policy on a host.  ***Since:*** vSphere API 4.1  | 
**name** | **str** | Power Policy Name.  ***Since:*** vSphere API 4.1  | 
**short_name** | **str** | Power Policy Short Name.  This is not localizable property which can be used to identify specific power managing policies like \&quot;custom\&quot; power policy. Custom power policy has short name set to \&quot;custom\&quot;.  ***Since:*** vSphere API 4.1  | 
**description** | **str** | Power Policy Description.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.host_power_policy import HostPowerPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostPowerPolicy from a JSON string
host_power_policy_instance = HostPowerPolicy.from_json(json)
# print the JSON string representation of the object
print HostPowerPolicy.to_json()

# convert the object into a dict
host_power_policy_dict = host_power_policy_instance.to_dict()
# create an instance of HostPowerPolicy from a dict
host_power_policy_form_dict = host_power_policy.from_dict(host_power_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


