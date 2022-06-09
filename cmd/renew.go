/*
Copyright © 2022 Robert Lützner

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

// renewCmd represents the renew command
var renewCmd = &cobra.Command{
	Use:   "renew",
	Short: "Restart the reminder period for a contact",
	Long: `Restart the reminder period for a contact.

#1 Tell friendly-reminder that you've talked to 'Omar Cabbage'.
friendly-reminder renew --name "Omar Cabbage"`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("renew called")
	},
}

func init() {
	rootCmd.AddCommand(renewCmd)
	renewCmd.Flags().String("name", "", "The name of the person you contacted")
	renewCmd.MarkFlagRequired("name")
}
