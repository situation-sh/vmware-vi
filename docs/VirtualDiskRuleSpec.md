# VirtualDiskRuleSpec

The set of virtual disks that are currently disabled  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_rule_type** | **str** | Type of the virtual disks rule.  The set of possible values are described in *VirtualDiskRuleSpecRuleType_enum*  ***Since:*** vSphere API 6.7  | 
**disk_id** | **List[int]** | The list of virtual disks for this rule.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_disk_rule_spec import VirtualDiskRuleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskRuleSpec from a JSON string
virtual_disk_rule_spec_instance = VirtualDiskRuleSpec.from_json(json)
# print the JSON string representation of the object
print VirtualDiskRuleSpec.to_json()

# convert the object into a dict
virtual_disk_rule_spec_dict = virtual_disk_rule_spec_instance.to_dict()
# create an instance of VirtualDiskRuleSpec from a dict
virtual_disk_rule_spec_form_dict = virtual_disk_rule_spec.from_dict(virtual_disk_rule_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


