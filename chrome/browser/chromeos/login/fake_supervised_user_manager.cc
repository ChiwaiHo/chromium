// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "chrome/browser/chromeos/login/fake_supervised_user_manager.h"

#include <string>

namespace chromeos {

FakeSupervisedUserManager::FakeSupervisedUserManager()  {}

FakeSupervisedUserManager::~FakeSupervisedUserManager() {
}

bool FakeSupervisedUserManager::HasSupervisedUsers(
    const std::string& manager_id) const {
  return false;
}

const User* FakeSupervisedUserManager::CreateUserRecord(
    const std::string& manager_id,
    const std::string& local_user_id,
    const std::string& sync_user_id,
    const base::string16& display_name) {
  return NULL;
}

std::string FakeSupervisedUserManager::GenerateUserId() {
  return std::string();
}

const User* FakeSupervisedUserManager::FindByDisplayName(
    const base::string16& display_name) const {
  return NULL;
}

const User* FakeSupervisedUserManager::FindBySyncId(
    const std::string& sync_id) const {
  return NULL;
}

std::string FakeSupervisedUserManager::GetUserSyncId(
    const std::string& managed_user_id) const {
  return std::string();
}

base::string16 FakeSupervisedUserManager::GetManagerDisplayName(
    const std::string& managed_user_id) const {
  return base::string16();
}

std::string FakeSupervisedUserManager::GetManagerUserId(
    const std::string& managed_user_id) const {
  return std::string();
}

std::string FakeSupervisedUserManager::GetManagerDisplayEmail(
    const std::string& managed_user_id) const {
  return std::string();
}

SupervisedUserAuthentication* FakeSupervisedUserManager::GetAuthentication() {
  return NULL;
}

void FakeSupervisedUserManager::LoadSupervisedUserToken(
    Profile * profile,
    const LoadTokenCallback& callback) {
  callback.Run("token");
}

}  // namespace chromeos
