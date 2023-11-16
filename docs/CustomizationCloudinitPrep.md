# CustomizationCloudinitPrep

Guest customization settings to customize a Linux guest operating system with raw cloud-init data.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** | Metadata includes the network, instance id and hostname that cloud-init processes to configure the VM.  It is in json or yaml format. The max size of the metadata is 524288 bytes. See detail information about &lt;a href&#x3D;\&quot;https://cloudinit.readthedocs.io/en/latest/topics/instancedata.html#\&quot;target&#x3D;\&quot;_blank\&quot;&gt;Instance Metadata&lt;/a&gt;.  ***Since:*** vSphere API 7.0.3.0  | 
**userdata** | **str** | Userdata is the user custom content that cloud-init processes to configure the VM.  The max size of the userdata is 524288 bytes. See detail information about &lt;a href&#x3D;\&quot;https://cloudinit.readthedocs.io/en/latest/topics/format.html\&quot;target&#x3D;\&quot;_blank\&quot;&gt;User-Data formats&lt;/a&gt;.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.customization_cloudinit_prep import CustomizationCloudinitPrep

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationCloudinitPrep from a JSON string
customization_cloudinit_prep_instance = CustomizationCloudinitPrep.from_json(json)
# print the JSON string representation of the object
print CustomizationCloudinitPrep.to_json()

# convert the object into a dict
customization_cloudinit_prep_dict = customization_cloudinit_prep_instance.to_dict()
# create an instance of CustomizationCloudinitPrep from a dict
customization_cloudinit_prep_form_dict = customization_cloudinit_prep.from_dict(customization_cloudinit_prep_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


