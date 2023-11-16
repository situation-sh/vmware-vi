# HostUnresolvedVmfsResolutionSpec

An unresolved VMFS volume is reported when one or more device partitions of volume are detected to have copies of extents of the volume.  Such copies can be created via replication or snapshots, for example. This data object type describes how to resolve an unbound VMFS volume. The SCSI device path for each of the VMFS volume extent should be specified. For the current release, only head-extent needs to be specified. In future releases, we will allow user to specify explicitly all the extents which makes up a new Vmfs Volume.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extent_device_path** | **List[str]** | List of device paths each specifying a VMFS extent.  One extent must be specified. This property is represented as a list to enable future enhancements to the interface.  ***Since:*** vSphere API 4.0  | 
**uuid_resolution** | **str** | When set to Resignature, new Uuid is assigned to the VMFS volume.  When set to &#39;forceMount&#39;, existing uuid is assigned to the Vmfs volume and Vmfs volumes metadata doesn&#39;t change.  See also *HostUnresolvedVmfsResolutionSpecVmfsUuidResolution_enum*.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_unresolved_vmfs_resolution_spec import HostUnresolvedVmfsResolutionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostUnresolvedVmfsResolutionSpec from a JSON string
host_unresolved_vmfs_resolution_spec_instance = HostUnresolvedVmfsResolutionSpec.from_json(json)
# print the JSON string representation of the object
print HostUnresolvedVmfsResolutionSpec.to_json()

# convert the object into a dict
host_unresolved_vmfs_resolution_spec_dict = host_unresolved_vmfs_resolution_spec_instance.to_dict()
# create an instance of HostUnresolvedVmfsResolutionSpec from a dict
host_unresolved_vmfs_resolution_spec_form_dict = host_unresolved_vmfs_resolution_spec.from_dict(host_unresolved_vmfs_resolution_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


