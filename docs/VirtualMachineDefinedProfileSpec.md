# VirtualMachineDefinedProfileSpec

Policy specification that carries a pre-defined Storage Policy to be associated with a Virtual Machine Home or a Virtual Disk object.  Such a pre-defined policy can be either be vSphere Storage Administrator defined or may come from a set of pre-defined policies from Storage Vendor.  Neither the association nor the policy data is persisted in Virtual Machine configuration. This data is managed by the an extension of Virtual Center (Storage Policy Based Management).  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Storage Policy Profile identification - Should be pbm.profileId but for implementation reasons, could not be.  ***Since:*** vSphere API 5.5  | 
**replication_spec** | [**ReplicationSpec**](ReplicationSpec.md) |  | [optional] 
**profile_data** | [**VirtualMachineProfileRawData**](VirtualMachineProfileRawData.md) |  | [optional] 
**profile_params** | [**List[KeyValue]**](KeyValue.md) | Parameterized Storage Profiles Extra configuration that is not expressed as a capability in the Profile definition.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_defined_profile_spec import VirtualMachineDefinedProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDefinedProfileSpec from a JSON string
virtual_machine_defined_profile_spec_instance = VirtualMachineDefinedProfileSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDefinedProfileSpec.to_json()

# convert the object into a dict
virtual_machine_defined_profile_spec_dict = virtual_machine_defined_profile_spec_instance.to_dict()
# create an instance of VirtualMachineDefinedProfileSpec from a dict
virtual_machine_defined_profile_spec_form_dict = virtual_machine_defined_profile_spec.from_dict(virtual_machine_defined_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


