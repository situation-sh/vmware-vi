# WillLoseHAProtection

This fault is reported when the execution of a storage vmotion or relocate operation would impact vSphere HA's ability to restart a VM.  For storage vmotion, this fault is reported when HA protection will be lost after the vmotion completes. Consequently, HA would not restart the VM if it subsequently failed. For relocate, relocate is not supported on VMs that failed before the operation is attempted and are in the process of being restarted at the time the operation is performed.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **str** | The steps the user can take to restore protection if the the operation is performed.  Values come from *WillLoseHAProtectionResolution_enum*.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.will_lose_ha_protection import WillLoseHAProtection

# TODO update the JSON string below
json = "{}"
# create an instance of WillLoseHAProtection from a JSON string
will_lose_ha_protection_instance = WillLoseHAProtection.from_json(json)
# print the JSON string representation of the object
print WillLoseHAProtection.to_json()

# convert the object into a dict
will_lose_ha_protection_dict = will_lose_ha_protection_instance.to_dict()
# create an instance of WillLoseHAProtection from a dict
will_lose_ha_protection_form_dict = will_lose_ha_protection.from_dict(will_lose_ha_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


