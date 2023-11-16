# VirtualMachineProfileDetailsDiskProfileDetails

Details of the policies associated with Virtual Disks.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **int** | Virtual disk ID.  ***Since:*** vSphere API 6.7  | 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | Storage profile associated with the Virtual Disk.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_profile_details_disk_profile_details import VirtualMachineProfileDetailsDiskProfileDetails

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineProfileDetailsDiskProfileDetails from a JSON string
virtual_machine_profile_details_disk_profile_details_instance = VirtualMachineProfileDetailsDiskProfileDetails.from_json(json)
# print the JSON string representation of the object
print VirtualMachineProfileDetailsDiskProfileDetails.to_json()

# convert the object into a dict
virtual_machine_profile_details_disk_profile_details_dict = virtual_machine_profile_details_disk_profile_details_instance.to_dict()
# create an instance of VirtualMachineProfileDetailsDiskProfileDetails from a dict
virtual_machine_profile_details_disk_profile_details_form_dict = virtual_machine_profile_details_disk_profile_details.from_dict(virtual_machine_profile_details_disk_profile_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


