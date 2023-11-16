# ComputeResourceHostSeedSpecSingleHostSpec

This data object contains a specification for a single candidate host for the host seeding operation.  If the candidate host is: \\- A new host not managed by vCenter Server: A *HostConnectSpec* needs to be provided. \\- A host managed by vCenter Server: A *HostSystem* needs to be provided. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_host_cnx_spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | [optional] 
**existing_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.compute_resource_host_seed_spec_single_host_spec import ComputeResourceHostSeedSpecSingleHostSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ComputeResourceHostSeedSpecSingleHostSpec from a JSON string
compute_resource_host_seed_spec_single_host_spec_instance = ComputeResourceHostSeedSpecSingleHostSpec.from_json(json)
# print the JSON string representation of the object
print ComputeResourceHostSeedSpecSingleHostSpec.to_json()

# convert the object into a dict
compute_resource_host_seed_spec_single_host_spec_dict = compute_resource_host_seed_spec_single_host_spec_instance.to_dict()
# create an instance of ComputeResourceHostSeedSpecSingleHostSpec from a dict
compute_resource_host_seed_spec_single_host_spec_form_dict = compute_resource_host_seed_spec_single_host_spec.from_dict(compute_resource_host_seed_spec_single_host_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


