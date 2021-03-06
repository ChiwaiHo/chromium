// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "chrome/browser/ui/window_sizer/window_sizer.h"

#include "chrome/browser/ui/host_desktop.h"

// This doesn't matter for aura, which has different tiling.
// static
const int WindowSizer::kWindowTilePixels = 10;

// static
gfx::Point WindowSizer::GetDefaultPopupOrigin(const gfx::Size& size,
                                              chrome::HostDesktopType type) {
  // TODO(skuhne): Check if this isn't needed anymore (since it is implemented
  // in WindowPositioner) and remove it.
  return gfx::Point();
}
