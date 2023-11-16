# HostDigestInfo

This data object type describes the digest information  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest_method** | **str** | Method in which the digest value is calculated.  The set of possible values is described in *HostDigestInfoDigestMethodType_enum*.  ***Since:*** vSphere API 4.0  | 
**digest_value** | **List[int]** | The variable length byte array containing the digest value calculated by the specified digestMethod.  ***Since:*** vSphere API 4.0  | 
**object_name** | **str** | The name of the object from which this digest value is calcaulated.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_digest_info import HostDigestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDigestInfo from a JSON string
host_digest_info_instance = HostDigestInfo.from_json(json)
# print the JSON string representation of the object
print HostDigestInfo.to_json()

# convert the object into a dict
host_digest_info_dict = host_digest_info_instance.to_dict()
# create an instance of HostDigestInfo from a dict
host_digest_info_form_dict = host_digest_info.from_dict(host_digest_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


