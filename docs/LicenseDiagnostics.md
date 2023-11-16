# LicenseDiagnostics

Deprecated as of vSphere API 4.0, this is not used by the system.  This data object type provides summary status and diagnostic information for *LicenseManager*.  Counters in this property can be reset to zero. The property specified as a discontinuity is used to determine when this last occurred.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_last_changed** | **datetime** | A timestamp of when sourceAvailable last changed state, expressed in UTC.  ***Since:*** VI API 2.5  | 
**source_lost** | **str** | Counter to track number of times connection to source was lost.  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5  | 
**source_latency** | **float** | Exponentially decaying average of the transaction time for license acquisition and routine communications with LicenseSource.  Units: milliseconds.  ***Since:*** VI API 2.5  | 
**license_requests** | **str** | Counter to track total number of licenses requested.  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5  | 
**license_request_failures** | **str** | Counter to track Total number of licenses requests that were not fulfilled (denied, timeout, or other).  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5  | 
**license_feature_unknowns** | **str** | Counter to track Total number of license features parsed from License source that are not recognized.  This value starts at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.  ***Since:*** VI API 2.5  | 
**op_state** | [**LicenseManagerStateEnum**](LicenseManagerStateEnum.md) |  | 
**last_status_update** | **datetime** | A timestamp of when opState was last updated.  ***Since:*** VI API 2.5  | 
**op_failure_message** | **str** | A human readable reason when optState reports Fault condition.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.license_diagnostics import LicenseDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseDiagnostics from a JSON string
license_diagnostics_instance = LicenseDiagnostics.from_json(json)
# print the JSON string representation of the object
print LicenseDiagnostics.to_json()

# convert the object into a dict
license_diagnostics_dict = license_diagnostics_instance.to_dict()
# create an instance of LicenseDiagnostics from a dict
license_diagnostics_form_dict = license_diagnostics.from_dict(license_diagnostics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


