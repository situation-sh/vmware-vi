# SoftRuleVioCorrectionDisallowed

The current DRS migration priority setting prevents generating a recommendation to correct the soft VM/Host affinity rules constraint violation for the VM so the violation will not be corrected.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm_name** | **str** | The vm for which the VM/Host soft affinity rules constraint violation is not being corrected by DRS.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.soft_rule_vio_correction_disallowed import SoftRuleVioCorrectionDisallowed

# TODO update the JSON string below
json = "{}"
# create an instance of SoftRuleVioCorrectionDisallowed from a JSON string
soft_rule_vio_correction_disallowed_instance = SoftRuleVioCorrectionDisallowed.from_json(json)
# print the JSON string representation of the object
print SoftRuleVioCorrectionDisallowed.to_json()

# convert the object into a dict
soft_rule_vio_correction_disallowed_dict = soft_rule_vio_correction_disallowed_instance.to_dict()
# create an instance of SoftRuleVioCorrectionDisallowed from a dict
soft_rule_vio_correction_disallowed_form_dict = soft_rule_vio_correction_disallowed.from_dict(soft_rule_vio_correction_disallowed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


