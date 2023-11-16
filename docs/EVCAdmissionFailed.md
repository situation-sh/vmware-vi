# EVCAdmissionFailed

The host does not satisfy the admission requirements for the Enhanced VMotion Compatibility mode of the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faults** | [**List[MethodFault]**](MethodFault.md) | The faults that caused this EVC test to fail (e.g.  FeatureRequirementsNotMet faults).  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.evc_admission_failed import EVCAdmissionFailed

# TODO update the JSON string below
json = "{}"
# create an instance of EVCAdmissionFailed from a JSON string
evc_admission_failed_instance = EVCAdmissionFailed.from_json(json)
# print the JSON string representation of the object
print EVCAdmissionFailed.to_json()

# convert the object into a dict
evc_admission_failed_dict = evc_admission_failed_instance.to_dict()
# create an instance of EVCAdmissionFailed from a dict
evc_admission_failed_form_dict = evc_admission_failed.from_dict(evc_admission_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


