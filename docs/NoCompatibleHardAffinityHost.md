# NoCompatibleHardAffinityHost

The cluster contains no hosts satisfying the hard VM/host affinity rules constraint for the VM.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The vm for which there are no compatible hard-affine hosts in the cluster.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.no_compatible_hard_affinity_host import NoCompatibleHardAffinityHost

# TODO update the JSON string below
json = "{}"
# create an instance of NoCompatibleHardAffinityHost from a JSON string
no_compatible_hard_affinity_host_instance = NoCompatibleHardAffinityHost.from_json(json)
# print the JSON string representation of the object
print NoCompatibleHardAffinityHost.to_json()

# convert the object into a dict
no_compatible_hard_affinity_host_dict = no_compatible_hard_affinity_host_instance.to_dict()
# create an instance of NoCompatibleHardAffinityHost from a dict
no_compatible_hard_affinity_host_form_dict = no_compatible_hard_affinity_host.from_dict(no_compatible_hard_affinity_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


