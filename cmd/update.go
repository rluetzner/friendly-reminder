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

// updateCmd represents the update command
var updateCmd = &cobra.Command{
	Use:   "update",
	Short: "Change settings for a contact",
	Long: `Change settings for a contact.

Examples:

#1 Rename 'Mom' to 'Mother'.
friendly-reminder update --name Mom --new-name Mother

#2 Remind about 'Mother' every 30 days.
friendly-reminder update --name Mother --days 30

#3 Update the last time you talked to 'Mother'.
friendly-reminder update --name Mother --last-contact 2022-06-09`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("update called")
	},
}

func init() {
	rootCmd.AddCommand(updateCmd)
	updateCmd.Flags().String("name", "", "The name of the person you want to update")
	updateCmd.MarkFlagRequired("name")
	updateCmd.Flags().String("new-name", "", "A new name for the person")
	updateCmd.Flags().Int("days", 0, "How many days between reminders")
	updateCmd.Flags().String("last-contact", "", "Date of your last contact in the format yyyy-mm-dd")
}
