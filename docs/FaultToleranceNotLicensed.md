# FaultToleranceNotLicensed

This fault is thrown when fault tolerance has not been licensed on the source or destination host.  It must be licensed on both hosts.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The host name  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.fault_tolerance_not_licensed import FaultToleranceNotLicensed

# TODO update the JSON string below
json = "{}"
# create an instance of FaultToleranceNotLicensed from a JSON string
fault_tolerance_not_licensed_instance = FaultToleranceNotLicensed.from_json(json)
# print the JSON string representation of the object
print FaultToleranceNotLicensed.to_json()

# convert the object into a dict
fault_tolerance_not_licensed_dict = fault_tolerance_not_licensed_instance.to_dict()
# create an instance of FaultToleranceNotLicensed from a dict
fault_tolerance_not_licensed_form_dict = fault_tolerance_not_licensed.from_dict(fault_tolerance_not_licensed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


