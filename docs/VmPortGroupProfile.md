# VmPortGroupProfile

The *VmPortGroupProfile* data object represents the subprofile for a port group that will be used by virtual machines.  Use the *ApplyProfile.policy* list for access to configuration data for the virtual machine port group profile. Use the *ApplyProfile.property* list for access to subprofiles, if any.  vSphere Servers use *Network* managed objects to represent virtual machine port groups in the vSphere inventory.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_port_group_profile import VmPortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of VmPortGroupProfile from a JSON string
vm_port_group_profile_instance = VmPortGroupProfile.from_json(json)
# print the JSON string representation of the object
print VmPortGroupProfile.to_json()

# convert the object into a dict
vm_port_group_profile_dict = vm_port_group_profile_instance.to_dict()
# create an instance of VmPortGroupProfile from a dict
vm_port_group_profile_form_dict = vm_port_group_profile.from_dict(vm_port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


