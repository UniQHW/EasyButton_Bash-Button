/*

 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.

 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.

 * Author       : Patrick Pedersen <ctx.xda@gmail.com>
 * Documentation:

 */

#include "EasyButton.h"
#include "BashButtonHandler.h"

/* EasyButton Data Pin */
const uint8_t EB_DATA = 3;

EasyButton *easy_button = new EasyButton(EB_DATA);
BashButtonHandler handler(easy_button);

void setup() {
  handler.init();
}

void loop() {
  handler.handle();
}
