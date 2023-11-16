# HostStorageElementInfo

Data object describing the operational status of various storage elements.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operational_info** | [**List[HostStorageOperationalInfo]**](HostStorageOperationalInfo.md) | Other information regarding the operational state of the storage element.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.host_storage_element_info import HostStorageElementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageElementInfo from a JSON string
host_storage_element_info_instance = HostStorageElementInfo.from_json(json)
# print the JSON string representation of the object
print HostStorageElementInfo.to_json()

# convert the object into a dict
host_storage_element_info_dict = host_storage_element_info_instance.to_dict()
# create an instance of HostStorageElementInfo from a dict
host_storage_element_info_form_dict = host_storage_element_info.from_dict(host_storage_element_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


