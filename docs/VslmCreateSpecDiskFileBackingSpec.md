# VslmCreateSpecDiskFileBackingSpec

Specification of the disk file backing of a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioning_type** | **str** | Provisioning type.  See also *BaseConfigInfoDiskFileBackingInfoProvisioningType_enum*  If unset, system will first look up the provisioning type specified in the policy. If still not found, the default *thin* will be used..  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vslm_create_spec_disk_file_backing_spec import VslmCreateSpecDiskFileBackingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmCreateSpecDiskFileBackingSpec from a JSON string
vslm_create_spec_disk_file_backing_spec_instance = VslmCreateSpecDiskFileBackingSpec.from_json(json)
# print the JSON string representation of the object
print VslmCreateSpecDiskFileBackingSpec.to_json()

# convert the object into a dict
vslm_create_spec_disk_file_backing_spec_dict = vslm_create_spec_disk_file_backing_spec_instance.to_dict()
# create an instance of VslmCreateSpecDiskFileBackingSpec from a dict
vslm_create_spec_disk_file_backing_spec_form_dict = vslm_create_spec_disk_file_backing_spec.from_dict(vslm_create_spec_disk_file_backing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


