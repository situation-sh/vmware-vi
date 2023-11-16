# ComplianceLocator

This dataObject contains information about location of applyProfile which was responsible for generation of a particular ComplianceExpression.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression_name** | **str** | Exression for which the Locator corresponds to  ***Since:*** vSphere API 4.0  | 
**apply_path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | 

## Example

```python
from vmware_vi.models.compliance_locator import ComplianceLocator

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceLocator from a JSON string
compliance_locator_instance = ComplianceLocator.from_json(json)
# print the JSON string representation of the object
print ComplianceLocator.to_json()

# convert the object into a dict
compliance_locator_dict = compliance_locator_instance.to_dict()
# create an instance of ComplianceLocator from a dict
compliance_locator_form_dict = compliance_locator.from_dict(compliance_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


