# ArrayOfComplianceResult

A boxed array of *ComplianceResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ComplianceResult]**](ComplianceResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_compliance_result import ArrayOfComplianceResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfComplianceResult from a JSON string
array_of_compliance_result_instance = ArrayOfComplianceResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfComplianceResult.to_json()

# convert the object into a dict
array_of_compliance_result_dict = array_of_compliance_result_instance.to_dict()
# create an instance of ArrayOfComplianceResult from a dict
array_of_compliance_result_form_dict = array_of_compliance_result.from_dict(array_of_compliance_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


