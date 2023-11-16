# VirtualDiskAntiAffinityRuleSpec

Pod-wide anit-affinity rule for virtual disks.  The set of virtual disks should be placed on different datastores.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_id** | **List[int]** | The list of virtual disks.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_disk_anti_affinity_rule_spec import VirtualDiskAntiAffinityRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskAntiAffinityRuleSpec from a JSON string
virtual_disk_anti_affinity_rule_spec_instance = VirtualDiskAntiAffinityRuleSpec.from_json(json)
# print the JSON string representation of the object
print VirtualDiskAntiAffinityRuleSpec.to_json()

# convert the object into a dict
virtual_disk_anti_affinity_rule_spec_dict = virtual_disk_anti_affinity_rule_spec_instance.to_dict()
# create an instance of VirtualDiskAntiAffinityRuleSpec from a dict
virtual_disk_anti_affinity_rule_spec_form_dict = virtual_disk_anti_affinity_rule_spec.from_dict(virtual_disk_anti_affinity_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


