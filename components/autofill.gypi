# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      # Private target only used in components/autofill.
      'target_name': 'autofill_regexes',
      'type': 'none',
      'actions': [{
        'action_name': 'autofill_regexes',
        'inputs': [
          '<(DEPTH)/build/escape_unicode.py',
          'autofill/browser/autofill_regex_constants.cc.utf8',
        ],
        'outputs': [
          '<(SHARED_INTERMEDIATE_DIR)/autofill_regex_constants.cc',
        ],
        'action': ['python', '<(DEPTH)/build/escape_unicode.py',
                   '-o', '<(SHARED_INTERMEDIATE_DIR)',
                   'autofill/browser/autofill_regex_constants.cc.utf8'],
      }],
    },
  ],
  'conditions': [
    ['OS != "ios"', {
      'targets': [
        {
          'target_name': 'autofill_common',
          'type': 'static_library',
          'dependencies': [
            '../base/base.gyp:base',
            '../content/content.gyp:content_common',
            '../ipc/ipc.gyp:ipc',
            '../third_party/WebKit/public/blink.gyp:blink',
            '../ui/ui.gyp:ui',
            '../url/url.gyp:url_lib',
          ],
          'conditions': [
            ['OS == "android"', {
              'dependencies': [
                'autofill_jni_headers',
              ],
            }],
          ],
          'include_dirs': [
            '..',
            '<(SHARED_INTERMEDIATE_DIR)/autofill'
          ],
          'sources': [
            'autofill/browser/android/auxiliary_profile_loader_android.cc',
            'autofill/browser/android/auxiliary_profile_loader_android.h',
            'autofill/browser/android/auxiliary_profiles_android.cc',
            'autofill/browser/android/auxiliary_profiles_android.h',
            'autofill/browser/android/component_jni_registrar.cc',
            'autofill/browser/android/component_jni_registrar.h',
            'autofill/browser/android/personal_data_manager_android.cc',
            'autofill/common/autocheckout_status.h',
            'autofill/common/autofill_constants.cc',
            'autofill/common/autofill_constants.h',
            'autofill/common/autofill_messages.h',
            'autofill/common/autofill_message_generator.cc',
            'autofill/common/autofill_message_generator.h',
            'autofill/common/autofill_pref_names.cc',
            'autofill/common/autofill_pref_names.h',
            'autofill/common/autofill_switches.cc',
            'autofill/common/autofill_switches.h',
            'autofill/common/form_data.cc',
            'autofill/common/form_data.h',
            'autofill/common/form_data_predictions.cc',
            'autofill/common/form_data_predictions.h',
            'autofill/common/form_field_data.cc',
            'autofill/common/form_field_data.h',
            'autofill/common/form_field_data_predictions.cc',
            'autofill/common/form_field_data_predictions.h',
            'autofill/common/password_form_fill_data.cc',
            'autofill/common/password_form_fill_data.h',
            'autofill/common/password_generation_util.cc',
            'autofill/common/password_generation_util.h',
            'autofill/common/web_element_descriptor.cc',
            'autofill/common/web_element_descriptor.h',
          ],
        },

        {
          # TODO(blundell): Eliminate this target; instead, have only the
          # autofill_content_browser target and a new top-level
          # autofill_shared target. crbug.com/247015
          'target_name': 'autofill_browser',
          'type': 'static_library',
          'include_dirs': [
            '..',
          ],
          'dependencies': [
            'autofill_common',
            'autofill_regexes',
            'encryptor',
            'user_prefs',
            'webdata_common',
            '../base/base.gyp:base',
            '../base/base.gyp:base_i18n',
            '../base/base.gyp:base_prefs',
            '../content/content.gyp:content_browser',
            '../content/content.gyp:content_common',
            '../google_apis/google_apis.gyp:google_apis',
            '../ipc/ipc.gyp:ipc',
            '../skia/skia.gyp:skia',
            '../sql/sql.gyp:sql',
            '../third_party/icu/icu.gyp:icui18n',
            '../third_party/icu/icu.gyp:icuuc',
            '../third_party/libjingle/libjingle.gyp:libjingle',
            '../third_party/libphonenumber/libphonenumber.gyp:libphonenumber',
            '../ui/ui.gyp:ui',
            '../url/url.gyp:url_lib',
            '../webkit/support/webkit_support.gyp:webkit_resources',

            'component_resources.gyp:component_resources',
          ],
          'sources': [
            'autofill/browser/address.cc',
            'autofill/browser/address.h',
            'autofill/browser/address_field.cc',
            'autofill/browser/address_field.h',
            'autofill/browser/autocomplete_history_manager.cc',
            'autofill/browser/autocomplete_history_manager.h',
            'autofill/browser/autofill-inl.h',
            'autofill/browser/autofill_country.cc',
            'autofill/browser/autofill_country.h',
            'autofill/browser/autofill_data_model.cc',
            'autofill/browser/autofill_data_model.h',
            'autofill/browser/autofill_download.cc',
            'autofill/browser/autofill_download.h',
            'autofill/browser/autofill_download_url.cc',
            'autofill/browser/autofill_download_url.h',
            'autofill/browser/autofill_external_delegate.cc',
            'autofill/browser/autofill_external_delegate.h',
            'autofill/browser/autofill_field.cc',
            'autofill/browser/autofill_field.h',
            'autofill/browser/autofill_ie_toolbar_import_win.cc',
            'autofill/browser/autofill_ie_toolbar_import_win.h',
            'autofill/browser/autofill_manager.cc',
            'autofill/browser/autofill_manager.h',
            'autofill/browser/autofill_manager_delegate.h',
            'autofill/browser/autofill_manager_test_delegate.h',
            'autofill/browser/autofill_metrics.cc',
            'autofill/browser/autofill_metrics.h',
            'autofill/browser/autofill_popup_delegate.h',
            'autofill/browser/autofill_profile.cc',
            'autofill/browser/autofill_profile.h',
            'autofill/browser/autofill_regex_constants.cc.utf8',
            'autofill/browser/autofill_regex_constants.h',
            'autofill/browser/autofill_regexes.cc',
            'autofill/browser/autofill_regexes.h',
            'autofill/browser/autofill_scanner.cc',
            'autofill/browser/autofill_scanner.h',
            'autofill/browser/autofill_server_field_info.h',
            'autofill/browser/autofill_type.cc',
            'autofill/browser/autofill_type.h',
            'autofill/browser/autofill_xml_parser.cc',
            'autofill/browser/autofill_xml_parser.h',
            'autofill/browser/contact_info.cc',
            'autofill/browser/contact_info.h',
            'autofill/browser/credit_card.cc',
            'autofill/browser/credit_card.h',
            'autofill/browser/credit_card_field.cc',
            'autofill/browser/credit_card_field.h',
            'autofill/browser/email_field.cc',
            'autofill/browser/email_field.h',
            'autofill/browser/field_types.h',
            'autofill/browser/form_field.cc',
            'autofill/browser/form_field.h',
            'autofill/browser/form_group.cc',
            'autofill/browser/form_group.h',
            'autofill/browser/form_structure.cc',
            'autofill/browser/form_structure.h',
            'autofill/browser/name_field.cc',
            'autofill/browser/name_field.h',
            'autofill/browser/password_autofill_manager.cc',
            'autofill/browser/password_autofill_manager.h',
            'autofill/browser/password_generator.cc',
            'autofill/browser/password_generator.h',
            'autofill/browser/personal_data_manager.cc',
            'autofill/browser/personal_data_manager.h',
            'autofill/browser/personal_data_manager_mac.mm',
            'autofill/browser/personal_data_manager_observer.h',
            'autofill/browser/phone_field.cc',
            'autofill/browser/phone_field.h',
            'autofill/browser/phone_number.cc',
            'autofill/browser/phone_number.h',
            'autofill/browser/phone_number_i18n.cc',
            'autofill/browser/phone_number_i18n.h',
            'autofill/browser/state_names.cc',
            'autofill/browser/state_names.h',
            'autofill/browser/validation.cc',
            'autofill/browser/validation.h',
            'autofill/browser/webdata/autofill_change.cc',
            'autofill/browser/webdata/autofill_change.h',
            'autofill/browser/webdata/autofill_entry.cc',
            'autofill/browser/webdata/autofill_entry.h',
            'autofill/browser/webdata/autofill_table.cc',
            'autofill/browser/webdata/autofill_table.h',
            'autofill/browser/webdata/autofill_webdata.h',
            'autofill/browser/webdata/autofill_webdata_backend.h',
            'autofill/browser/webdata/autofill_webdata_backend_impl.cc',
            'autofill/browser/webdata/autofill_webdata_backend_impl.h',
            'autofill/browser/webdata/autofill_webdata_service.cc',
            'autofill/browser/webdata/autofill_webdata_service.h',
            'autofill/browser/webdata/autofill_webdata_service_observer.h',

            # This file is generated by the autofill_regexes action.
            '<(SHARED_INTERMEDIATE_DIR)/autofill_regex_constants.cc',
          ],

          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [4267, ],
        },

        {
          # Protobuf compiler / generate rule for Autofill's risk integration.
          'target_name': 'autofill_content_risk_proto',
          'type': 'static_library',
          'sources': [
            'autofill/content/browser/risk/proto/fingerprint.proto',
          ],
          'variables': {
            'proto_in_dir': 'autofill/content/browser/risk/proto',
            'proto_out_dir': 'components/autofill/content/browser/risk/proto',
          },
          'includes': [ '../build/protoc.gypi' ]
        },
       {
         'target_name': 'autofill_content_test_util',
         'type': 'static_library',
         'sources': [
           'autofill/content/browser/wallet/wallet_test_util.cc',
           'autofill/content/browser/wallet/wallet_test_util.h',
         ],
         'include_dirs': [ '..' ],
       },
       {
          'target_name': 'autofill_content_browser',
          'type': 'static_library',
          'include_dirs': [
            '..',
          ],
          'dependencies': [
            'autofill_browser',
            'autofill_common',
            'autofill_content_risk_proto',
            'autofill_regexes',
            'encryptor',
            'user_prefs',
            'webdata_common',
            '../base/base.gyp:base',
            '../base/base.gyp:base_i18n',
            '../base/base.gyp:base_prefs',
            '../content/content.gyp:content_browser',
            '../content/content.gyp:content_common',
            '../google_apis/google_apis.gyp:google_apis',
            '../ipc/ipc.gyp:ipc',
            '../skia/skia.gyp:skia',
            '../sql/sql.gyp:sql',
            '../third_party/icu/icu.gyp:icui18n',
            '../third_party/icu/icu.gyp:icuuc',
            '../third_party/libjingle/libjingle.gyp:libjingle',
            '../third_party/libphonenumber/libphonenumber.gyp:libphonenumber',
            '../ui/ui.gyp:ui',
            '../url/url.gyp:url_lib',
            '../webkit/support/webkit_support.gyp:webkit_resources',

            'component_resources.gyp:component_resources',
          ],
          'sources': [
            'autofill/content/browser/autocheckout/whitelist_manager.cc',
            'autofill/content/browser/autocheckout/whitelist_manager.h',
            'autofill/content/browser/autocheckout_manager.cc',
            'autofill/content/browser/autocheckout_manager.h',
            'autofill/content/browser/autocheckout_page_meta_data.cc',
            'autofill/content/browser/autocheckout_page_meta_data.h',
            'autofill/content/browser/autocheckout_request_manager.cc',
            'autofill/content/browser/autocheckout_request_manager.h',
            'autofill/content/browser/risk/fingerprint.cc',
            'autofill/content/browser/risk/fingerprint.h',
            'autofill/content/browser/wallet/encryption_escrow_client.cc',
            'autofill/content/browser/wallet/encryption_escrow_client.h',
            'autofill/content/browser/wallet/encryption_escrow_client_observer.h',
            'autofill/content/browser/wallet/form_field_error.cc',
            'autofill/content/browser/wallet/form_field_error.h',
            'autofill/content/browser/wallet/full_wallet.cc',
            'autofill/content/browser/wallet/full_wallet.h',
            'autofill/content/browser/wallet/instrument.cc',
            'autofill/content/browser/wallet/instrument.h',
            'autofill/content/browser/wallet/required_action.cc',
            'autofill/content/browser/wallet/required_action.h',
            'autofill/content/browser/wallet/wallet_address.cc',
            'autofill/content/browser/wallet/wallet_address.h',
            'autofill/content/browser/wallet/wallet_client.cc',
            'autofill/content/browser/wallet/wallet_client.h',
            'autofill/content/browser/wallet/wallet_client_delegate.h',
            'autofill/content/browser/wallet/wallet_items.cc',
            'autofill/content/browser/wallet/wallet_items.h',
            'autofill/content/browser/wallet/wallet_service_url.cc',
            'autofill/content/browser/wallet/wallet_service_url.h',
            'autofill/content/browser/wallet/wallet_signin_helper.cc',
            'autofill/content/browser/wallet/wallet_signin_helper.h',
          ],

          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [4267, ],
        },

        {
          'target_name': 'autofill_content_renderer',
          'type': 'static_library',
          'include_dirs': [
            '..',
          ],
          'dependencies': [
            'autofill_common',
            '../base/base.gyp:base',
            '../content/content.gyp:content_renderer',
            '../content/content.gyp:content_common',
            '../ipc/ipc.gyp:ipc',
            '../skia/skia.gyp:skia',

            'component_resources.gyp:component_resources',
          ],
          'sources': [
            'autofill/content/renderer/autofill_agent.cc',
            'autofill/content/renderer/autofill_agent.h',
            'autofill/content/renderer/form_autofill_util.cc',
            'autofill/content/renderer/form_autofill_util.h',
            'autofill/content/renderer/form_cache.cc',
            'autofill/content/renderer/form_cache.h',
            'autofill/content/renderer/page_click_listener.h',
            'autofill/content/renderer/page_click_tracker.cc',
            'autofill/content/renderer/page_click_tracker.h',
            'autofill/content/renderer/password_autofill_agent.cc',
            'autofill/content/renderer/password_autofill_agent.h',
            'autofill/content/renderer/password_generation_manager.cc',
            'autofill/content/renderer/password_generation_manager.h',
          ],
          # TODO(jschuh): crbug.com/167187 fix size_t to int truncations.
          'msvs_disabled_warnings': [4267, ],
        },
      ],
    }],
    ['OS == "android"', {
      'targets': [
        {
          'target_name': 'autofill_java',
          'type': 'none',
          'dependencies': [
            '../base/base.gyp:base',
            '../content/content.gyp:content_java',
          ],
          'variables': {
            'java_in_dir': 'autofill/browser/android/java',
          },
          'includes': [ '../build/java.gypi' ],
        },
        {
          'target_name': 'autofill_jni_headers',
          'type': 'none',
          'sources': [
            'autofill/browser/android/java/src/org/chromium/components/browser/autofill/PersonalAutofillPopulator.java',
          ],
          'variables': {
            'jni_gen_package': 'autofill',
          },
          'includes': [ '../build/jni_generator.gypi' ],
        },
      ],
    }],
  ],
}
