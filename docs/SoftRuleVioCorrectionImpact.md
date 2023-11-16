# SoftRuleVioCorrectionImpact

DRS has determined that correcting the soft VM/Host affinity rules constraint violation for the VM impacts respecting cluster constraints or performance goals so the violation will not be corrected.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The vm for which the VM/Host soft affinity rules constraint violation is not being corrected by DRS.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.soft_rule_vio_correction_impact import SoftRuleVioCorrectionImpact

# TODO update the JSON string below
json = "{}"
# create an instance of SoftRuleVioCorrectionImpact from a JSON string
soft_rule_vio_correction_impact_instance = SoftRuleVioCorrectionImpact.from_json(json)
# print the JSON string representation of the object
print SoftRuleVioCorrectionImpact.to_json()

# convert the object into a dict
soft_rule_vio_correction_impact_dict = soft_rule_vio_correction_impact_instance.to_dict()
# create an instance of SoftRuleVioCorrectionImpact from a dict
soft_rule_vio_correction_impact_form_dict = soft_rule_vio_correction_impact.from_dict(soft_rule_vio_correction_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


