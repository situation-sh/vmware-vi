# MissingBmcSupport

A MissingBmcSuppport fault is thrown when a host's BMC doesn't support IPMI.  BMC (Board Management Controller) is a piece of hardware required for IPMI.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.missing_bmc_support import MissingBmcSupport

# TODO update the JSON string below
json = "{}"
# create an instance of MissingBmcSupport from a JSON string
missing_bmc_support_instance = MissingBmcSupport.from_json(json)
# print the JSON string representation of the object
print MissingBmcSupport.to_json()

# convert the object into a dict
missing_bmc_support_dict = missing_bmc_support_instance.to_dict()
# create an instance of MissingBmcSupport from a dict
missing_bmc_support_form_dict = missing_bmc_support.from_dict(missing_bmc_support_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


