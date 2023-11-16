# PnicUplinkProfile

The *PnicUplinkProfile* data object specifies the mapping between a physical NIC and an uplink port.  The *ApplyProfile.policy* property contains the configuration data values.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.pnic_uplink_profile import PnicUplinkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PnicUplinkProfile from a JSON string
pnic_uplink_profile_instance = PnicUplinkProfile.from_json(json)
# print the JSON string representation of the object
print PnicUplinkProfile.to_json()

# convert the object into a dict
pnic_uplink_profile_dict = pnic_uplink_profile_instance.to_dict()
# create an instance of PnicUplinkProfile from a dict
pnic_uplink_profile_form_dict = pnic_uplink_profile.from_dict(pnic_uplink_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


