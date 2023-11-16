# VlanProfile

The *VlanProfile* data object represents the VLAN identifier subprofile.  The *ApplyProfile.policy* property contains the configuration data values for the VLAN identifier.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vlan_profile import VlanProfile

# TODO update the JSON string below
json = "{}"
# create an instance of VlanProfile from a JSON string
vlan_profile_instance = VlanProfile.from_json(json)
# print the JSON string representation of the object
print VlanProfile.to_json()

# convert the object into a dict
vlan_profile_dict = vlan_profile_instance.to_dict()
# create an instance of VlanProfile from a dict
vlan_profile_form_dict = vlan_profile.from_dict(vlan_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


