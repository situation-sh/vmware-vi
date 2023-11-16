# VslmCreateSpecRawDiskMappingBackingSpec

Specification of the rdm backing of a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | Unique identifier of the LUN accessed by the raw disk mapping.  ***Since:*** vSphere API 6.5  | 
**compatibility_mode** | **str** | The compatibility mode of the raw disk mapping (RDM).  This must be specified when a new virtual disk with an RDM backing is created.  See also *VirtualDiskCompatibilityMode_enum*.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.vslm_create_spec_raw_disk_mapping_backing_spec import VslmCreateSpecRawDiskMappingBackingSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VslmCreateSpecRawDiskMappingBackingSpec from a JSON string
vslm_create_spec_raw_disk_mapping_backing_spec_instance = VslmCreateSpecRawDiskMappingBackingSpec.from_json(json)
# print the JSON string representation of the object
print VslmCreateSpecRawDiskMappingBackingSpec.to_json()

# convert the object into a dict
vslm_create_spec_raw_disk_mapping_backing_spec_dict = vslm_create_spec_raw_disk_mapping_backing_spec_instance.to_dict()
# create an instance of VslmCreateSpecRawDiskMappingBackingSpec from a dict
vslm_create_spec_raw_disk_mapping_backing_spec_form_dict = vslm_create_spec_raw_disk_mapping_backing_spec.from_dict(vslm_create_spec_raw_disk_mapping_backing_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


